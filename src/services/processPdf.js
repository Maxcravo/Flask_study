const fs = require("fs");
const pdfParser = require("pdf2json")
const path = require('path')

// Supondo aqui que já sei o path do arquivo e só preciso do nome path = src/public/uploads/
const processPdf = async (fileName) => {
  const pdf = new pdfParser();
  let pdfPath = path.join(process.cwd(), "public/uploads/");
  
  pdf.on("pdfParser_dataError", (errData) =>
    console.error(errData.parserError)
  );
  pdf.on("pdfParser_dataReady", (pdfData) => {
    fs.writeFile(
    "./pdf2json/test/F1040EZ.json", {flag: "w+"},
    JSON.stringify(pdfData),
    (data) => console.log(data)
    );
  });
  
  pdf.loadPDF(pdfPath + "testando_1_2_3.pdf");
}

processPdf();