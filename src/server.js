const express = require("express");
const multer = require("multer");
const cors = require("cors");
const path = require("path");
const fs =  require("fs")
const processPdf = require("./services/processPdf");

const app = express();
app.use(cors());
app.use(express.static("public"))
let pdfName = ""

const uploadsDir = path.join(process.cwd(), "public/uploads");

if (!fs.existsSync(uploadsDir)) {
  fs.mkdirSync(uploadsDir, { recursive: true });
  console.log(`Created uploads directory: ${uploadsDir}`);
}

const storage = multer.diskStorage({ // Aqui basicamente setamos o destino do arquivo que o usuário enviar.
  destination: function (req, file, cb) { // a função que vai definir o destino do arquivo vai ter como cb o destino do arquivo e null que seria a resposta de erro.
    cb(null, uploadsDir); 
  },
  filename: function (req, file, cb) {
    cb(null, file.originalname); // Aqui estamos definindo o nome do arquivo que o usuário enviou, roubei a ideia do vídeo que eu vi no youtube.
    cb(null, pdfName = file.originalname); 
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

const PORT = 3001;
app.listen(PORT,()=>{
  console.log(`Servidor rodando na porta ${PORT}`);
})

//TODO AQUI EU QUERO ALÉM DE ENVIAR O ARQUIVO IREI JÁ TRATAR UTILIZANDO A FUNÇÃO processPdf
// Criar o endpoint para uploads de arquivos
//! NUNCA ESQUECER QUE TENHO QUE GARANTIR QUE A FUNÇÃO DA ROTA SEJA ASYNC SE NÃO SEMPRE VOU RECEBER PROMISSE {<}
app.post("/api/multer", upload.single("file"), async (req, res) => {
  try {
    if (!req.file) {
    return  res.status(400).send("Arquivo não encontrado"); // caso o usuário não envie o arquivo retornamos error 400
    }
    let pdf_text = await processPdf(req.file.filename);
    console.log(pdf_text);    
    res.status(200).json({ // Caso tudo tenha sido enviado corretamente, retornamos o status 200 e o json com infos do arquivo.
      message: "arquivo enviado com sucesso",
      text: `string do pdf ${pdf_text}`
    })
  } catch (error) {
    res.status(500).json({error: error.messages});
  }
});

