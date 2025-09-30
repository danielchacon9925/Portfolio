// ISR seats a global flag when data is ready

// Write main loop that waits for flag, processes data and clears it safety


volatile int flag = 0;


int main(){

while(1){
    if (flag){
        // Process data
        flag = 0;
    }
}

} 