param ($path, $name)

mkdir $path/$name
Set-Location $path/$name

write-host ">> Creating solution file"
dotnet new sln -n $name

write-host ">> Creating new web project"
dotnet new emptyweb -n $name.Website 
write-host ">> Adding newly created Website project to $name solution"
dotnet sln $name.sln add ./$name.Website/$name.Website.csproj

write-host ">> Creating new Core project"
dotnet new emptylibrary -n $name.Core
write-host ">> Adding newly created Core project to $name solution"
dotnet sln $name.sln add ./$name.Core/$name.Core.csproj

write-host ">> Creating new Infrastructure project"
dotnet new emptylibrary -n $name.Infrastructure
write-host ">> Adding newly created Infrastructure project to $name solution"
dotnet sln $name.sln add ./$name.Infrastructure/$name.Infrastructure.csproj

write-host ">> Creating new DW project"
dotnet new emptylibrary -n $name.DW 
write-host ">> Adding newly created DW project to $name solution"
dotnet sln $name.sln add ./$name.DW/$name.DW.csproj

write-host ">> Creating new Infractucture test project"
dotnet new xunit -n "$name.Infractucture.Tests"
write-host ">> Adding newly created test project to $name.Infractucture solution"
dotnet sln $name.sln add ./$name.Infractucture.Tests/$name.Infractucture.Tests.csproj
write-host ">> Adding test project reference to net472 project"
dotnet add ./$name.Infractucture.Tests/$name.Infractucture.Tests.csproj reference ./$name.Infractucture/$name.Infractucture.csproj

write-host ">> Adding latest dynamicweb Admin to the Website project"
dotnet add ./$name.Website/$name.Website.csproj package Dynamicweb.Admin -https://www.myget.org/F/dynamicweb-packages/api/v3/index.json

write-host ">> Running Restore"
dotnet restore
write-host ">> Running Build"
dotnet build
write-host ">> Running Tests"
dotnet test