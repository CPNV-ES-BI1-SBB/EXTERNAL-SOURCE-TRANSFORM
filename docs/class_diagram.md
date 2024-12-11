# Class Diagram
```mermaid
---
title: External source transform
---
classDiagram
    
    class TransformBuilder {
        - originalData: any[]
        - transformedData: any[]
        + build(): any[]
        + setInitialStation(): void
        + setDepartureStation(): void
        + getTransformedData(): any[]
    }
    
    class AWSService {
        - connectionString: string
        - destinationName: string
        + connect(): void
        + disconnect(): void
        + load(originPath: string, destinationPath: string): void
    }
    
    class S3SDK { }
    
    class DestinationNotFoundError { }
    
    class OriginNotFoundError { }
    
    class TransformError { }
    
    TransformBuilder --> AWSService
    AWSService --> S3SDK
    AWSService --> DestinationNotFoundError
    AWSService --> OriginNotFoundError
    TransformBuilder --> TransformError
```