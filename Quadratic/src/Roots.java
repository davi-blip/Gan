//written by Jianyuan Gan


public class Roots {
    //create two complex instances to store variables
    private Complex4 x1;
    private Complex4 x2;

    public Roots(float a, float b, float c){
        double formulas = b * b - (4 * a * c);
        if (formulas >= 0) {
            double root1 = (-b + Math.sqrt(formulas)) / (2 * a);
            double root2 = (-b - Math.sqrt(formulas)) / (2 * a);
            this.x1 = new Complex4(root1,0);
            this.x2 = new Complex4(root2,0);
        }else if(formulas <0){
            double root1 = -b / (2*a);
            double root2 =  Math.sqrt(-formulas)/ (2*a);
            this.x1 = new Complex4(root1,root2);
            this.x2 = new Complex4(root1,-root2);
        }
    }
    public double getX1(){
        return this.x1.getRealPart();
    }
    public double getX2(){
        return this.x2.getRealPart();
    }
    public double getReal(){
        return this.x1.getRealPart();
    }
    public double getImage(){
        return this.x2.getImaginaryPart();
    }

    public String toString() {

            return this.x1.toString() + "\n"+this.x2.toString();
        }
}


