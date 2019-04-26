# IoArgoprojWorkflowV1alpha1Artifact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive** | [**IoArgoprojWorkflowV1alpha1ArchiveStrategy**](IoArgoprojWorkflowV1alpha1ArchiveStrategy.md) | Archive controls how the artifact will be saved to the artifact repository. | [optional] 
**archive_logs** | **bool** | ArchiveLogs indicates if the container logs should be archived | [optional] 
**artifactory** | [**IoArgoprojWorkflowV1alpha1ArtifactoryArtifact**](IoArgoprojWorkflowV1alpha1ArtifactoryArtifact.md) | Artifactory contains artifactory artifact location details | [optional] 
**_from** | **str** | From allows an artifact to reference an artifact from a previous step | [optional] 
**git** | [**IoArgoprojWorkflowV1alpha1GitArtifact**](IoArgoprojWorkflowV1alpha1GitArtifact.md) | Git contains git artifact location details | [optional] 
**global_name** | **str** | GlobalName exports an output artifact to the global scope, making it available as &#39;{{workflow.outputs.artifacts.XXXX}} and in workflow.status.outputs.artifacts | [optional] 
**hdfs** | [**IoArgoprojWorkflowV1alpha1HDFSArtifact**](IoArgoprojWorkflowV1alpha1HDFSArtifact.md) | HDFS contains HDFS artifact location details | [optional] 
**http** | [**IoArgoprojWorkflowV1alpha1HTTPArtifact**](IoArgoprojWorkflowV1alpha1HTTPArtifact.md) | HTTP contains HTTP artifact location details | [optional] 
**mode** | **int** | mode bits to use on this file, must be a value between 0 and 0777 set when loading input artifacts. | [optional] 
**name** | **str** | name of the artifact. must be unique within a template&#39;s inputs/outputs. | 
**optional** | **bool** | Make Artifacts optional, if Artifacts doesn&#39;t generate or exist | [optional] 
**path** | **str** | Path is the container path to the artifact | [optional] 
**raw** | [**IoArgoprojWorkflowV1alpha1RawArtifact**](IoArgoprojWorkflowV1alpha1RawArtifact.md) | Raw contains raw artifact location details | [optional] 
**s3** | [**IoArgoprojWorkflowV1alpha1S3Artifact**](IoArgoprojWorkflowV1alpha1S3Artifact.md) | S3 contains S3 artifact location details | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


