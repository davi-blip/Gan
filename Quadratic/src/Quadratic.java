//written by Jianyuan Gan

public class Quadratic {
    private float a;
    private float b;
    private float c;
    /**
     * @param a coefficients
     * @param b coefficients
     * @param c coefficients
     */
    public Quadratic(float a, float b, float c){
        this.a = a;
        this.b = b;
        this.c = c;
    }
    //Accessor method
    /**
     * @param value set up the A value
     */
    public void setA(float value) {
         this.a= value;
    }

    /**
     * @param value set up the B value
     */
    public void setB(float value) {
        this.b = value;
    }

    /**
     * @param value set up the C value
     */
    public void setC(float value){
        this.c = value;
    }

    /**
     * @return value of A
     */
    public float getA() {
        return this.a;
    }

    /**
     * @return value of B
     */
    public float getB() {
        return this.b;
    }

    /**
     * @return return Value of C
     */
    public float getC() {
        return this.c;
    }

    /**
     * @return generate a new quadratic function by using addition
     */
    public Quadratic add(Quadratic other){
        return new Quadratic(this.a + other.getA(), this.b + other.getB(),this.c + other.getC());
    }

    /**
     * @return a new quadratic function
     */
    public Quadratic subtract(Quadratic other){
        return new Quadratic(this.a - other.getA(), this.b - other.getB(),this.c - other.getC());
    }

    /**
     * @return A method to get two values of x1, x2
     */
    public Roots findRoots(){
        return new Roots(this.a,this.b,this.c);
    }

    /**
     * @return a String representation of the current quadratic function
     */
    public String toString(){
        String s = " ";
        if(this.b < 0 && this.c<0){
            s = (int)this.a +"x^2"+(int)this.b+"x"+(int)this.c;
        }else if(this.b>0 && this.c>0){
            s = (int)this.a +"x^2"+"+"+(int)this.b+"x"+"+"+(int)this.c;
        }else if(this.b>0 && this.c<0){
            s = (int)this.a + "x^2"+"+"+(int)this.b+"x"+(int)this.c;
        }else if(this.b<0 && this.c>0){
            s = (int)this.a+"x^2"+(int)this.b+"x"+"+"+(int)this.c;
        }return s;
    }


    /**
     * @param other equation
     * @return if this.equation is not equals to other return false. Otherwise, return true.
     */
    public boolean equals(Object other){
        if (other instanceof Quadratic) {
            Quadratic temp = (Quadratic) other;
            return a == temp.getA() && b == temp.getB() && c == temp.getC();
        }
        return false;
    }

    public static void main(String[] args) {
        Quadratic other1,other2,other3,other4;
        other1 = new Quadratic(1,2,3);
        other2 = new Quadratic(1,2,3);
        System.out.println("boolean"+" "+other1.equals(other2));
        System.out.println("toString"+" "+other1);
        System.out.println("addition"+" "+other1.add(other2));
        System.out.println("subtraction"+" "+other1.subtract(other2));
        System.out.println("Imagination"+" "+other1.findRoots().getImage());
        System.out.println("real"+" "+other1.findRoots().getReal());
        System.out.println("root1"+" "+other1.findRoots().getX1());
        System.out.println("root2"+" "+other1.findRoots().getX2());
        System.out.println(other1.findRoots().toString());
        System.out.println();
        other3 = new Quadratic(1,-3,4);
        other4 = new Quadratic(2,-3,5);
        System.out.println("boolean"+" "+other3.equals(other4));
        System.out.println("toString"+" "+other3);
        System.out.println("addition"+" "+other3.add(other4));
        System.out.println("subtraction"+" "+other3.subtract(other4));
        System.out.println("Imagination"+" "+other3.findRoots().getImage());
        System.out.println("real"+" "+other3.findRoots().getReal());
        System.out.println("root1"+" "+other3.findRoots().getX1());
        System.out.println("root2"+" "+other3.findRoots().getX2());
        System.out.println(other1.findRoots().toString());
    }
}

