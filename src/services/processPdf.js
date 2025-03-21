"use server"
const fs = require("fs");
const pdfParser = require("pdf2json")
const path = require('path')
const pdf = require('pdf-parse');

// async function processPdf (fileName)  {
//   let pdfPath = path.join(process.cwd(), "/public/uploads/");
//   let dataBuffer = fs.readFileSync(pdfPath + fileName);
//   await pdf(dataBuffer).then((data) => {
//     // Aqui  pegamos o texto do arquivo PDF e podemos tranformar em JSON
//     // console.log(data.text);
//     return data.text;
//   }).catch((error) => {
//     console.log(error);
//   });
// } 

// module.exports = processPdf;
// -------------------------------------------------

async function processPdf (fileName)  {
  try{
  let pdfPath = path.join(process.cwd(), "/public/uploads/");
  let dataBuffer = fs.readFileSync(pdfPath + fileName);
  const data = await pdf(dataBuffer)
  return data.text;
  } catch (error) {
    console.log(error);
  }
} 

module.exports = processPdf;