from app.ingest import ingest_document

file_path = "data/documents/dii-summer-guidelines-april-2025.pdf"

ingest_document(file_path)

print("PDF document ingested successfully.")
