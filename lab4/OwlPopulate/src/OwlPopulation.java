import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class OwlPopulation {
    private String fileName;
    private Owl[] data;


    public void populateData() throws FileNotFoundException{
        File f = new File(fileName);
        Scanner scanner = new Scanner(f);

        int numLines = 0;
        while(scanner.hasNextLine()){
            numLines++;
            String s = scanner.nextLine();
        }
        scanner.close();

        data = new Owl[numLines];   //data is is allocated the exact amount of space it needs
        scanner = new Scanner(f);

        for(int i = 0;i<numLines;i++){
            String[] a = scanner.nextLine().split(",");
            data[i] = new Owl(a[0],Integer.parseInt(a[1]),Double.parseDouble(a[2]));
        }

        //TODO: Populate the data with owls constructed from the lines of the file given
    }

    public OwlPopulation(String fileName) throws FileNotFoundException{
        this.fileName = fileName;
        populateData();
        //TODO: Populate the class variables in OwlPopulation
    }

    public double averageAge(){
        int sumOfAge = 0;
        for(int i = 0; i < data.length;i++){
            sumOfAge += data[i].getAge();
        }
        return sumOfAge;
    }

    public int getYoungest(){
        int getYoungestIndex = 0;
        for(int i = 0; i < data.length;i++){
            if(data[i].getAge()<data[getYoungestIndex].getAge()){
                getYoungestIndex = i;
            }
        }
        return data[getYoungestIndex].getAge();
    }

    public double getHeaviest(){
        int getHeaviestIndex = 0;
        for(int i = 0; i < data.length;i++){
            if(data[getHeaviestIndex].getWeight()>data[i].getWeight()){
                getHeaviestIndex = i;
            }
        }
        return data[getHeaviestIndex].getWeight();
    }

    public String toString(){
        String s = "";
        s += "the avg age:"+averageAge()+"this is the youngest:"+getYoungest()+"this the heaviest:"+getHeaviest();
        return s;
    }

    public boolean containsOwl(Owl other){
        for(int i =0; i< data.length;i++){
            if(data[i].equals(other)==true){
                    return true;
            }
        }return false;
    }
    public void merge(OwlPopulation other){
        //TODO: a brief overview of what you can do to implement this method is given below:

        //1) determine (and store) the distinct owls in the other population.
        int distinct = 0;//count in other array


        for(int i = 0; i < data.length;i++) {
            if (containsOwl(other.data[i]) == false) {
                distinct++;//current owl
            }
        }
        //2) make a new data array to hold the correct number of owls for the merged population
        Owl[] newOwl = new Owl[distinct+data.length];
        for(int j = 0; j < data.length; j ++) {
            newOwl[j] = data[j];//store the current owl
        }
        int idx = 0;
        for(int a= 0; a <other.data.length;a++){
            newOwl[distinct + idx] = data[a];//store the other owl into the current array
            idx++;
        }
        newOwl = this.data;
    }

            //3) copy over the distinct owls from each population to the data array

        //4) set the new data array to "this" data (where is the merged population? what happens to the original populations?)


    public int popSize(){
        return data.length;
    }
    public static void main(String[] args) {
        try {

            //The following should run when you are complete. Feel free to comment out as you see fit while you work.
            OwlPopulation pop1 = new OwlPopulation("owlPopulation1.csv");
            System.out.println(pop1);
            System.out.println(pop1.popSize());

            OwlPopulation pop2 = new OwlPopulation("owlPopulation2.csv");
            System.out.println(pop2);
            System.out.println(pop2.popSize());

            pop1.merge(pop2);
            System.out.println(pop1);
            System.out.println(pop1.popSize());

        }
        catch (FileNotFoundException f){
            System.out.println("File not found.");
        }
    }


}
