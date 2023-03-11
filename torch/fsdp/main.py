import datetime

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP


class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = nn.Linear(256, 256)
        self.l2 = nn.Linear(256, 2)

    def forward(self, x):
        h = self.l1(x)
        h = F.relu(h)
        h = self.l2(h)
        return h


# torch.cuda.set_device(device_id)
print("Hi form pytorch", torch.__version__)
my_module = MyModule()

backend = "mpi"  # TODO: use class for more controll

process_group = torch.distributed.init_process_group(
    backend,
    init_method=None,
    timeout=datetime.timedelta(seconds=1800),
    world_size=-1,
    rank=-1,
    store=None,
    group_name='',
    pg_options=None)

sharded_module = FSDP(
    my_module,
    process_group=process_group,
    sharding_strategy=None,
    cpu_offload=None,
    auto_wrap_policy=None,
    backward_prefetch=None,
    mixed_precision=None,
    ignored_modules=None,
    param_init_fn=None,
    device_id=None,
    sync_module_states=False,
    forward_prefetch=False,
    limit_all_gathers=False)
# sharded_module = my_module
optim = torch.optim.Adam(sharded_module.parameters(), lr=0.0001)
x = torch.rand(256)
logits = sharded_module(x)
print(logits)
loss = logits.sum()
loss.backward()
optim.step()
