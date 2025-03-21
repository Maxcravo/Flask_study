"use server"
import multer from "multer";
import { NextResponse } from "next/server";
import os from "os";
import path, { resolve } from "path";
import {promises as fs} from "fs";
import { rejects } from "assert";

const storage = multer.diskStorage({ // Aqui basicamente setamos o destino do arquivo que o usuário enviar.
  destination: function (req, file, cb) { // a função que vai definir o destino do arquivo vai ter como cb o destino do arquivo e null que seria a resposta de erro.
    cb(null, path.join(process.cwd(), "public/uploads")); 
  },
  filename: function (req, file, cb) {
    cb(null, new Date().toISOString() + "-" + file.originalname); // Aqui estamos definindo o nome do arquivo que o usuário enviou, roubei a ideia do vídeo que eu vi no youtube.
  }
})

const filter = (req, file, cb) => { // Função que vai fazer com que o multer apenas aceite arquivo pdf. 
  if (file.mimetype === "application/pdf" ) {
    cb(null, true); // Se o usuário enviar um pdf, ele vai ser aceito corretamente.
  }
  else {
    cb(new Error("Apenas são aceitos arquivos PDF"), false); 
  }
}

const upload = multer({
  storage: storage,
  limits: {
    fileSize: 1024 * 1024 * 5 // 5mb tamanho máximo
  },
  fileFilter: filter

})
// Criamos uma função middleware para que possamos usar o async/await no arquivo page.js
function middleware(req, res, fn) {
  return new Promise((resolve, reject) => {
    fn(req, res, (result) => {
      if (result instanceof Error) {
        return reject(result);
      }
      return resolve(result);
    })
  })
}
// Aqui definimios a rota que vai receber o arquivo e enviar para a pasta uploads usando o multer.
export async function POST(req){
  // Recebemos a resposta
  const response = new NextResponse();

  const tempDir = os.tmpdir();
  const filePath = path.join(tempDir, "file.pdf");


}


export default upload; 