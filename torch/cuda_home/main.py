from torch.utils.cpp_extension import CUDA_HOME, _find_cuda_home
print(CUDA_HOME)
print(_find_cuda_home())
