"""Aviso por e-mail quando o cliente conclui o briefing.

O briefing (front) gera o PDF no navegador do cliente e envia para
POST {API}/briefings/{token}/concluido. Esta rota manda o PDF anexado
para os e-mails do escritório.

Configuração (variáveis de ambiente):
  NOTIFY_EMAILS   e-mails separados por vírgula (padrão abaixo)
  SMTP_HOST       ex.: smtp.gmail.com
  SMTP_PORT       ex.: 587
  SMTP_USER       conta que envia (ex.: o Gmail do escritório)
  SMTP_PASSWORD   no Gmail, uma "senha de app" (não a senha normal)

No front, preencher zzNotifyApi (hoje vazio) com o endereço da API do site.

Uso no FastAPI:  app.include_router(notify.router)
"""
import os
import smtplib
from email.message import EmailMessage

from fastapi import APIRouter, File, HTTPException, UploadFile

NOTIFY_EMAILS = [
    e.strip()
    for e in os.getenv(
        "NOTIFY_EMAILS", "levybezerradomingos00@gmail.com,pbstudioarq@gmail.com"
    ).split(",")
    if e.strip()
]
MAX_PDF = 15 * 1024 * 1024

router = APIRouter()


def build_message(token: str, filename: str, pdf: bytes) -> EmailMessage:
    nome = filename.removeprefix("Briefing ").removesuffix(".pdf") or token
    msg = EmailMessage()
    msg["Subject"] = f"Briefing preenchido e finalizado: {nome}"
    msg["From"] = os.getenv("SMTP_USER", "")
    msg["To"] = ", ".join(NOTIFY_EMAILS)
    msg.set_content(
        f"Olá, equipe Trioma.\n\n{nome} preencheu e finalizou o briefing de interiores.\n"
        "O PDF com todas as respostas está em anexo.\n"
    )
    msg.add_attachment(pdf, maintype="application", subtype="pdf", filename=filename)
    return msg


@router.post("/briefings/{token}/concluido")
async def briefing_concluido(token: str, pdf: UploadFile = File(...)):
    data = await pdf.read()
    # validação na entrada: só PDF e com tamanho limitado
    if not data.startswith(b"%PDF") or len(data) > MAX_PDF:
        raise HTTPException(400, "PDF inválido")
    msg = build_message(token, pdf.filename or f"Briefing {token}.pdf", data)
    host = os.getenv("SMTP_HOST")
    if not host:
        print(f"[notify] SMTP não configurado; e-mail para {NOTIFY_EMAILS} não enviado")
        return {"enviado": False}
    with smtplib.SMTP(host, int(os.getenv("SMTP_PORT", "587"))) as s:
        s.starttls()
        s.login(os.environ["SMTP_USER"], os.environ["SMTP_PASSWORD"])
        s.send_message(msg)
    return {"enviado": True}


if __name__ == "__main__":  # autoteste rápido: python notify.py
    m = build_message("abc", "Briefing Ana.pdf", b"%PDF-1.4 teste")
    assert m["Subject"] == "Briefing preenchido e finalizado: Ana"
    assert "pbstudioarq@gmail.com" in m["To"] and "levybezerradomingos00@gmail.com" in m["To"]
    assert any(p.get_filename() == "Briefing Ana.pdf" for p in m.iter_attachments())
    print("ok")
