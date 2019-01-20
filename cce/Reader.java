import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


/** Class for buffered reading int and double values */
class Reader {
    static BufferedReader reader;
    static StringTokenizer tokenizer;

    /** call this method to initialize reader for InputStream */
    static void init(InputStream input) {
        reader = new BufferedReader(
                new InputStreamReader(input) );
        tokenizer = new StringTokenizer("");
    }

    /** get next word */
    static String next() throws IOException {
        while ( ! tokenizer.hasMoreTokens() ) {
            //TODO add check for eof if necessary
            tokenizer = new StringTokenizer(
                    reader.readLine() );
        }
        return tokenizer.nextToken();
    }

    static int nextInt() throws IOException {
        return Integer.parseInt( next() );
    }

    static double nextDouble() throws IOException {
        return Double.parseDouble( next() );
    }

    public static void main(String[] args) throws IOException{
        // write your code here

        Reader.init(System.in);

        int k = Reader.nextInt();
        int s = Reader.nextInt();
        int count = 0;
        for (int x = 0; x <= k; x++){
            for(int y = 0; y <= k; y++){
                for(int z = 0; z <=k; z++){
                    if(x + y + z == s){
                        count = count + 1;
                    }
                }
            }
        }
        System.out.println(count);
        
            
    }

}