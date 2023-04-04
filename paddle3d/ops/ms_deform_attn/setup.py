from paddle.utils.cpp_extension import CUDAExtension, setup

setup(
    name='ms_deform_attn',
    ext_modules=CUDAExtension(
        sources=['ms_deform_attn.cc', 'ms_deform_attn.cu'],
        extra_compile_args={'nvcc': ['-arch=sm_60']},
    ))
