from os import path

import ds_api_on_docker

base_path = path.dirname(path.dirname(ds_api_on_docker.__file__))
workspace_path = path.join(base_path, 'workspace')
data_path = path.join(workspace_path, 'data')
models_path = path.join(workspace_path, 'models')
