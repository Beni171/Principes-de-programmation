import javax.jws.WebParam;
import javax.jws.WebService;
import javax.jws.WebMethod;

@WebService(targetNamespace="http://www.polytech.fr")
public class MyService {
    @WebMethod(operationName="convertir")
    public double conversion(double mt) {
        return mt * 0.9;
    }
    public double somme (@WebParam(name="parametre1") double a, double b){
        return a*b;
    }

    public Etudiant getEtudiant(int identifiant){
        return new Etudiant(1, "Mario", 19);
    }
}