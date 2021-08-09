# Powershell Scripts

## Solution Starter 
This script will create a new dotnet project of a defined template in a designed folder.

### Steps

1. Create and move to the target folder
2. Creates a new .sln file
3. Creates a new project from the designated template
4. Creates a new test project
5. Build and Run Tests


### How to use

```Terminal
.\new_solution_init.ps1 -path <path> -project <template> -name <projectname>
```

### Example

```Terminal
.\new_solution_init.ps1 -path . -project webapi -name Project
```