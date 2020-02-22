public class Owl{
    private String name;
    private int age;
    private double weight;

    public Owl(String name, int age, double weight){
        this.name = name;
        this.age = age;
        this.weight = weight;
    }
    public void setName(String name1){
        name = name1;
    }
    public void setAge(int age1){
        age = age1;
    }
    public void setWeight(double weight1){
        weight = weight1;
    }
    public String getName(){
        return name;
    }
    public int getAge(){
        return age;
    }
    public double getWeight(){
        return weight;
    }
    public boolean equals(Owl other){
        Owl temp;
        boolean same = false;
        if(name.equals(other.getName())&&age == other.getAge()&& weight == other.getWeight()){
            return true;
        }return false;
    }

    public static void main(String[] args) {
        Owl s1,s2;
        s1 = new Owl("ha",1,1.2);
        s2 = new Owl("he",1,1.3);
        System.out.println(s1.equals(s2));
    }
}
