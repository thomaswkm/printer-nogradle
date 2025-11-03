module ImageApp {
    // Definimos una secuencia de bytes
    sequence<byte> ByteSeq;

    interface ColorService {
        // Recibe una imagen en bytes y devuelve su versión en blanco y negro
        ByteSeq Color2BW(ByteSeq image);
    };
};

