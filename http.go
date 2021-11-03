//server for linux 
//golang
// go run http.go  终端输入即可运行
package main
 
import (
 "fmt"
 "io"
 "net/http"
 "os"
 
 
 
)
 
const uploadPath = "./upload"
 
func handleUploadFile(w http.ResponseWriter, r *http.Request) {
 r.ParseMultipartForm(100)
 mForm := r.MultipartForm
 
 r.ParseMultipartForm(1024)
    fmt.Println("post file:", r.MultipartForm)

    io.WriteString(w, "表单提交成功")
    
 for k, _ := range mForm.File {
  // k is the key of file part
  file, fileHeader, err := r.FormFile(k)
  if err != nil {
   fmt.Println("inovke FormFile error:\n", err)
   return
  }
  defer file.Close()
  fmt.Printf("the uploaded file: name[%s], size[%d], header[%#v]n\n",
   fileHeader.Filename, fileHeader.Size, fileHeader.Header)
 
  // store uploaded file into local path
  localFileName := uploadPath + "/" + fileHeader.Filename
  out, err := os.Create(localFileName)
  if err != nil {
   fmt.Printf("failed to open the file %s for writing\n", localFileName)
   return
  }
  defer out.Close()
  _, err = io.Copy(out, file)
  if err != nil {
   fmt.Printf("copy file err:%sn\n", err)
   return
  }
  fmt.Printf("file %s uploaded okn\n", fileHeader.Filename)
 
 }
}


func main() {
 http.HandleFunc("/upload", handleUploadFile)
 
 fmt.Println("server has opend, Ctry+C to stop")
 
 http.ListenAndServe(":8888", nil)
 
}
