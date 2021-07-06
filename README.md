# Weather Cloud Formation templates via SAM Template and Stackery

The cloud formation templates is generated using AWS SAM template, generally used for managing serverless applications

Here is an overview of the files:

```text
.
├── deployHooks/                       <-- Directory for storing deployment hooks
├── .gitignore                         <-- Gitignore for Stackery
├── .stackery-config.yaml              <-- Default CLI parameters for root directory
├── README.md                          <-- This README file
└── template.yaml                      <-- SAM infrastructure-as-code template
```
# Weather Script via AWS Lambda solution

This solution involves a serverless AWS Lambda application, that runs every 60 minutes.

https://github.com/rsheyeah-bbc/demostackery/tree/main/src/Function
