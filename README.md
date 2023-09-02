#
# Yaml-Merger

Simple Python script "designed" to make merging Kubernetes YAML files a ***breeze***. I've personally used it once (I believe that doing it manually would be quicker).

**Key Features**:
- Utilizes the power of `glob` to match file name patterns using `*` (representing one or more characters).
- Works exclusively with files ending in `.yaml`.
- If the file named like output file exists, it won't be overwritten.

**Flags**:
- `-o=OUTPUT_FILE_NAME`: Specifies the output YAML file name. If not explicitly defined, the output file will be named `output.yaml` by default.
- `-h, --help`: Prints *manual*.
- `-v`: Displays the names of both the files matched by `glob` and the merged files.

**Example Usage** (on files in the repository):
- `python main.py *`: Merges all `yaml` files.
- `python main.py k8s-d* -v -o=deployments`: Merges only files starting with `k8s-d`, prints their names, and creates a combined YAML file named `deployments`.

