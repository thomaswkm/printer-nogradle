import sys
import io
import Ice
import ImageApp  # generado por slice2py
from PIL import Image


class ColorServiceI(ImageApp.ColorService):
    def Color2BW(self, image_bytes, current=None):
        try:
            print("📥 Imagen recibida. Tamaño en bytes:", len(image_bytes))

            # Convertimos bytes -> imagen
            img = Image.open(io.BytesIO(image_bytes))
            print(
                "🖼️ Imagen cargada correctamente. Formato:",
                img.format,
                "Tamaño:",
                img.size,
            )

            # Convertimos a blanco y negro
            print("⚙️ Procesando imagen (convirtiendo a blanco y negro)...")
            bw = img.convert("L")

            # Convertimos la imagen de nuevo a bytes
            output = io.BytesIO()
            bw.save(output, format="JPEG")
            print("📤 Imagen procesada y convertida a bytes para enviar.")

            return output.getvalue()
        except Exception as e:
            print(f"❌ Error en Color2BW: {e}")
            return b""  # devolvemos bytes vacíos si algo falla  # devolvemos bytes vacíos si algo falla


class Server(Ice.Application):
    def run(self, args):
        broker = self.communicator()
        adapter = broker.createObjectAdapterWithEndpoints(
            "ColorAdapter", "tcp -h 10.147.18.5 -p 10000"
        )
        servant = ColorServiceI()
        adapter.add(servant, broker.stringToIdentity("ColorService"))
        adapter.activate()
        print("Servidor Ice escuchando en puerto 10000 Zero Tier...")
        self.shutdownOnInterrupt()
        broker.waitForShutdown()
        return 0


if __name__ == "__main__":
    sys.exit(Server().main(sys.argv))
