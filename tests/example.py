from ghostdata.cleaner import GhostData

# Remove metadata from an image
clean_image = GhostData.clean("test.jpg")
print(f"Cleaned image saved at: {clean_image}")

# Remove metadata from a PDF
clean_pdf = GhostData.clean("document.pdf")
print(f"Cleaned PDF saved at: {clean_pdf}")
