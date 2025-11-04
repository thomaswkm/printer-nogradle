const Ice = require("ice").Ice;
const ImageApp = require("./ColorService").ImageApp;
const fs = require("fs");

(async function () {
  let communicator;

  try {
    // Inicializar ICE
    communicator = Ice.initialize();

    // Crear proxy al objeto remoto
    const base = communicator.stringToProxy(
      "ColorService:tcp -h 10.147.18.5 -p 10000"
    );
    const service = await ImageApp.ColorServicePrx.checkedCast(base);

    if (!service) {
      console.error("Proxy inválido o no se pudo conectar al servicio.");
      return;
    }

    console.log("Conectado al servidor ZeroC Ice ✅");

    // Leer imagen local (por ejemplo, 'input.jpg')
    const inputPath = "./images/input.jpg";
    if (!fs.existsSync(inputPath)) {
      console.error("❌ No se encontró input.jpg en el directorio actual");
      return;
    }

    const imageBytes = fs.readFileSync(inputPath);

    console.log(`Enviando imagen de ${imageBytes.length} bytes...`);

    // Llamar al método remoto Color2BW
    const bwBytes = await service.Color2BW(new Uint8Array(imageBytes));

    // Guardar la imagen en disco
    const outputPath = "./output_bw.jpg";
    fs.writeFileSync(outputPath, Buffer.from(bwBytes));

    console.log(`✅ Imagen procesada guardada en ${outputPath}`);
  } catch (ex) {
    console.error("❌ Error:", ex.toString());
    process.exitCode = 1;
  } finally {
    if (communicator) {
      await communicator.destroy();
    }
  }
})();
