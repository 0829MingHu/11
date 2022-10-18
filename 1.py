import os
import numpy as np
from tqdm import tqdm

input_path = '/home/chenj0g/rgb_flow/flow_feature_npz/'
out_path = '/home/chenj0g/rgb_flow/convert/flow_feature_npz/'
for fi in tqdm(os.listdir(input_path)):
        a = np.load(os.path.join(input_path, fi))
        print(a['feature'].shape, a['frame_cnt'])

        #np.save(os.path.join(out_path, str(a['video_name'])), a['feature'][0])