"use client"
import Image from "next/image";
import styles from "./page.module.css";
import upload from "../../utils/multer";
import { useState } from "react";

export default function Home() {
  const [file, setFile] = useState(null)

  const handlefileChange = (e) => {
    setFile(e.target.files[0]);
    console.log("cheguei");
    console.log(file);
  }

  const handlefile = async (e) => { // Função para organizar o processo de envio de arquivos
    e.preventDefault();
    console.log(file);
    // console.log("cheguei");

    if (!file) {
      console.log("Arquivo não encontrado");
      return;
    }
    if (file.type !== "application/pdf") {
      console.log("Somente arquivos PDF são aceitos");
      return;
    }
    const formData = new FormData();
    formData.append("file", file);
    console.log("Arquivo de texto:", formData);

    try {
      const response = await fetch("http://localhost:3001/api/multer", {
        method: "POST",
        body: formData,
      });
      const data_file = await response.json();
      console.log("Arquivo enviado com sucesso", data_file);

    } catch (error) {
      console.log(error);
    }
  }



  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <form onSubmit={handlefile}  encType="multipart/form-data">
        <input  accept="application/pdf" type="file" name="file" onChange={handlefileChange} />
        
        <input type="submit" value="enviar"  />
        </form> 

      </main>
    </div>
  );
}
