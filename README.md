# shared-generated
 
 Generated Go and Python code for the API contracts. CI generates it
 and overwrites it on every publish, so do not edit it here.
 
 ## Layout
 
 | Path | Contents |
 |---|---|
 | `go/` | Go module `github.com/versegeek/shared-generated/go` |
 | `go/grpc/` | gRPC code generated from Protobuf |
 | `go/rest/` | REST code generated from OpenAPI 3.0 |
 | `python/grpc/` | gRPC code generated from Protobuf |
 
 ## Go
 
 ```bash
 go get github.com/versegeek/shared-generated/go@latest
 ```
 
 ```go
 import (
     "github.com/versegeek/shared-generated/go/grpc/<domain>/v1" // package <domain>v1
     "github.com/versegeek/shared-generated/go/rest/<domain>/v1" // package <domain>V1
 )
 
 // Your code here...
 ```
 
## Python
 
 ```bash
 pip install "shared-generated @ git+https://github.com/versegeek/shared-generated.git#subdirectory=python"
 # or
 uv add "git+https://github.com/versegeek/shared-generated.git#subdirectory=python"
 ```
 
 ```python
 from <domain>.v1 import <name>_pb2, <name>_pb2_grpc
 
 # Your code here...
 ``` 
 

