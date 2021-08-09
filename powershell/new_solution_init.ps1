param ($path, $project, $name)

mkdir $path/$name
Set-Location $path/$name

write-host ">> Creating solution file"
dotnet new sln -n $name
write-host ">> Creating new $project project"
dotnet new $project -n $name
write-host ">> Adding newly created $project to $name solution"
dotnet sln $name.sln add ./$name/$name.csproj

write-host ">> Creating new test project"
dotnet new xunit -n "$name.Tests"
write-host ">> Adding newly created test project to $name solution"
dotnet sln $name.sln add ./$name.Tests/$name.Tests.csproj
write-host ">> Adding test project reference to $project project"
dotnet add ./$name.Tests/$name.Tests.csproj reference ./$name/$name.csproj

write-host ">> Running Build"
dotnet build
write-host ">> Running Tests"
dotnet test