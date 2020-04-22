# UploadAttachmentOptions

Options for uploading files for attachments. When sending emails with the API that require attachments first upload each attachment. Then use the returned attachment ID in your `SendEmailOptions` when sending an email. This way you can use attachments multiple times once they have been uploaded.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base64_contents** | **str** | Base64 encoded string of file contents | [optional] 
**content_type** | **str** | Optional contentType for file. For instance &#x60;application/pdf&#x60; | [optional] 
**filename** | **str** | Optional filename to save upload with | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


