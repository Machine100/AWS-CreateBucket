
import boto3
s3resource = boto3.resource('s3')

bucket = s3resource.Bucket('word')   #Create a Bucket Sub-resource. Sub-resources are methods that create 
                                     #a new instance of a child resource. The resource's identifiers get 
                                     #passed along to the child.  