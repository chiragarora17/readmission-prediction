mkdir -p dataset_diabetes
cp ../../dataset_diabetes/*.npy dataset_diabetes/
cp ../../dataset_diabetes/*.sav dataset_diabetes/
cp ../../dataset_diabetes/*.p dataset_diabetes/
nohup python Api.py False > server.log 2>&1  &
