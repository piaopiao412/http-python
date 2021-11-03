package main
import (
"fmt"
"io"
"net/http"
)


func handler(w http.ResponseWriter, r *http.Request) {
http.SetCookie(w, &http.Cookie{Name: "pa", Value: "dps"})
r.Header.Add("server", "go/1.0")
io.WriteString(w, "myserver is running!")
fmt.Printf("r.header=%+v,r.usr.string=%+v,r.url.path=%+v\n", r.Header, r.URL.String(), r.URL.Path)
r.ParseForm()
d := r.Form
fmt.Println(d)


}


func main() {
http.HandleFunc("/agent", handler)


http.ListenAndServe("192.168.203.83:8888", nil)}
