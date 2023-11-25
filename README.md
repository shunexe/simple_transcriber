# How to use

1. Set up
```shell
docker compose up -d
```
2. Put your audio file in the `audio` directory
3. Run the script
```shell
docker compose exec app python main.py
```
4. Check the result
Transcript will be saved as `output.txt` in the `src` directory
