�	/�$��?/�$��?!/�$��?	��TI�-@��TI�-@!��TI�-@"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$/�$��?��+e�?A�O��n�?Yu���?*	23333�x@2F
Iterator::Model���H.�?!�۾:O@)���Q��?1�³��N@:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMapjM�?!C5(��z3@)]m���{�?1� ��h2@:Preprocessing2u
>Iterator::Model::ParallelMapV2::Zip[0]::FlatMap::Prefetch::Map�Pk�w�?!���kVZ,@)a2U0*��?1�*���#@:Preprocessing2�
LIterator::Model::ParallelMapV2::Zip[0]::FlatMap::Prefetch::Map::FiniteRepeat"��u���?!���Ŋ@)��ǘ���?1!d����@:Preprocessing2Z
#Iterator::Model::ParallelMapV2::Zip+��η?!ڃ^L_�7@)S�!�uq{?1�?U�?:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat��ׁsF�?!(��z�1@)S�!�uq{?1�?U�?:Preprocessing2U
Iterator::Model::ParallelMapV2��H�}m?!:@��m_�?)��H�}m?1:@��m_�?:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensor-C��6j?!m�����?)-C��6j?1m�����?:Preprocessing2p
9Iterator::Model::ParallelMapV2::Zip[0]::FlatMap::Prefetcha2U0*�c?!�*����?)a2U0*�c?1�*����?:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[5]::TensorSlice-C��6Z?!m�����?)-C��6Z?1m�����?:Preprocessing2�
SIterator::Model::ParallelMapV2::Zip[0]::FlatMap::Prefetch::Map::FiniteRepeat::Range����MbP?!y��uQ�?)����MbP?1y��uQ�?:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[4]::TensorSlice-C��6*?!m�����?)-C��6*?1m�����?:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
both�Your program is MODERATELY input-bound because 14.8% of the total step time sampled is waiting for input. Therefore, you would need to reduce both the input time and other time.no*no9 �TI�-@>Look at Section 3 for the breakdown of input time on the host.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	��+e�?��+e�?!��+e�?      ��!       "      ��!       *      ��!       2	�O��n�?�O��n�?!�O��n�?:      ��!       B      ��!       J	u���?u���?!u���?R      ��!       Z	u���?u���?!u���?JCPU_ONLYY �TI�-@b Y      Y@q~H��]P@"�
both�Your program is MODERATELY input-bound because 14.8% of the total step time sampled is waiting for input. Therefore, you would need to reduce both the input time and other time.b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"T
Rtensorflow_stats (identify the time-consuming operations executed on the CPU_ONLY)"Z
Xtrace_viewer (look at the activities on the timeline of each CPU_ONLY in the trace view)*�
�<a href="https://www.tensorflow.org/guide/data_performance_analysis" target="_blank">Analyze tf.data performance with the TF Profiler</a>*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2I
=type.googleapis.com/tensorflow.profiler.GenericRecommendation
nono:
Refer to the TF2 Profiler FAQb�65.4533% of Op time on the host used eager execution. Performance could be improved with <a href="https://www.tensorflow.org/guide/function" target="_blank">tf.function.</a>2"CPU: B 