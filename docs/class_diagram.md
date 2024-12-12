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
    
    class S3Service {
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
    
    TransformBuilder --> S3Service
    S3Service --> S3SDK
    S3Service --> DestinationNotFoundError
    S3Service --> OriginNotFoundError
    TransformBuilder --> TransformError
```