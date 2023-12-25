Experimenter
- Setup
    - New : To create a new experiment
    - Open : 
    - Results Destination 
        - Output to what type of file : csv, arff, jdbc db
    1. Experiment Type(Step 1) : cross-validation, data split, ...
    2. Iteration Control(Step 2) : Run the experiment how many time
    3. Datasets(Step 3) : How many datasets need to run
    4. Algorithms(Step 4) : Use how many/what algorithm
- Run
    1. Start(Step 5)
- Analyse
    1. Experiment(Step 6)
    2. Perform test(Step 7)
    - std. deviations : 越大每次實驗差距越大， 標準差越小代表每次實驗差距越小

Multiple experiment
1. Open Experimenter
2. Setup -> New
    - Add new dataset
    - Add new algorithms, add all wanted algorithms
3. Run -> Start
4. Analyse -> Experiment -> Perform test
- Result : **v** (Significantly better), **\*** (Significantly worse)