
[int]$num = Read-Host "¿Qué/cual tabla quieres?"
$numeros = 0..9
$mul = 0

foreach ($n in $numeros)
{
	$mul = $num * $n
	Write-Host "$num * $n = $mul"
}
