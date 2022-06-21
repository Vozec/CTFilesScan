$saved = ''
$path = "windows_installed.txt"
if (Test-Path -Path $path -PathType Leaf)
  {
    $saved = Get-Content $path
  }
  
Get-ChildItem "windows" -Filter *.ps1 | 
    Foreach-Object {
      if($saved -contains $_)
        {
          Write-Output "$_ already installed"
        }
      else
        {
          Write-Output "#######################################"
          Write-Output "Running $_ "
          Write-Output "#######################################"
          & "./windows/$_"
          Write-Output "$_" >> "$path"
        }     
    }

