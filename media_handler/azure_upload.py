from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def upload_image_to_azure(local_image_path, container_name, blob_name, connection_string):
    try:
        # Create a BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # Create a ContainerClient
        container_client = blob_service_client.get_container_client(container_name)

        # Upload the image to Azure Blob Storage
        with open(local_image_path, "rb") as data:
            container_client.upload_blob(name=blob_name, data=data)

        # Generate a URL for the uploaded image
        blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name}"

        return blob_url

    except Exception as e:
        return {"Message": str(e)}

# # Example usage:
# if __name__ == "__main__":
#     local_image_path = "path_to_local_image.jpg"  # Replace with the path to your local image
#     container_name = "your_container_name"        # Replace with your Azure Blob Storage container name
#     blob_name = "image.jpg"                       # Replace with the name you want for the image in Azure
#     connection_string = "your_connection_string"  # Replace with your Azure Storage Account connection string

#     image_url = upload_image_to_azure(local_image_path, container_name, blob_name, connection_string)
    
#     if not image_url.startswith("Error"):
#         print(f"Image uploaded successfully. URL: {image_url}")
#     else:
#         print(f"Error uploading
