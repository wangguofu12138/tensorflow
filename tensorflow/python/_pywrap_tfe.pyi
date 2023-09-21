# Copyright 2023 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from typing import ClassVar, Dict, List

TFE_DEVICE_PLACEMENT_EXPLICIT: TFE_ContextDevicePlacementPolicy
TFE_DEVICE_PLACEMENT_SILENT: TFE_ContextDevicePlacementPolicy
TFE_DEVICE_PLACEMENT_SILENT_FOR_INT32: TFE_ContextDevicePlacementPolicy
TFE_DEVICE_PLACEMENT_WARN: TFE_ContextDevicePlacementPolicy
TF_ATTR_BOOL: TF_AttrType
TF_ATTR_FLOAT: TF_AttrType
TF_ATTR_FUNC: TF_AttrType
TF_ATTR_INT: TF_AttrType
TF_ATTR_PLACEHOLDER: TF_AttrType
TF_ATTR_SHAPE: TF_AttrType
TF_ATTR_STRING: TF_AttrType
TF_ATTR_TENSOR: TF_AttrType
TF_ATTR_TYPE: TF_AttrType

class EagerContextThreadLocalData:
    device_name: object
    device_spec: object
    executor
    function_call_options: object
    invoking_op_callbacks: bool
    is_eager: bool
    op_callbacks: object
    scope_name: object
    def __init__(self, py_eager_context, is_eager, device_spec) -> None: ...

class TFE_CancellationManager:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_ContextDevicePlacementPolicy:
    __members__: ClassVar[dict] = ...  # read-only
    TFE_DEVICE_PLACEMENT_EXPLICIT: ClassVar[TFE_ContextDevicePlacementPolicy] = ...
    TFE_DEVICE_PLACEMENT_SILENT: ClassVar[TFE_ContextDevicePlacementPolicy] = ...
    TFE_DEVICE_PLACEMENT_SILENT_FOR_INT32: ClassVar[TFE_ContextDevicePlacementPolicy] = ...
    TFE_DEVICE_PLACEMENT_WARN: ClassVar[TFE_ContextDevicePlacementPolicy] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TFE_ContextOptions:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_Executor:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringBoolGauge0:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringBoolGauge1:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringBoolGauge2:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringBoolGaugeCell:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringBuckets:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringCounter0:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringCounter1:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringCounter2:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringCounterCell:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringIntGauge0:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringIntGauge1:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringIntGauge2:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringIntGaugeCell:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringSampler0:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringSampler1:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringSampler2:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringSamplerCell:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringStringGauge0:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringStringGauge1:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringStringGauge2:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringStringGauge3:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringStringGauge4:
    def __init__(self, *args, **kwargs) -> None: ...

class TFE_MonitoringStringGaugeCell:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_AttrType:
    __members__: ClassVar[dict] = ...  # read-only
    TF_ATTR_BOOL: ClassVar[TF_AttrType] = ...
    TF_ATTR_FLOAT: ClassVar[TF_AttrType] = ...
    TF_ATTR_FUNC: ClassVar[TF_AttrType] = ...
    TF_ATTR_INT: ClassVar[TF_AttrType] = ...
    TF_ATTR_PLACEHOLDER: ClassVar[TF_AttrType] = ...
    TF_ATTR_SHAPE: ClassVar[TF_AttrType] = ...
    TF_ATTR_STRING: ClassVar[TF_AttrType] = ...
    TF_ATTR_TENSOR: ClassVar[TF_AttrType] = ...
    TF_ATTR_TYPE: ClassVar[TF_AttrType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TF_Buffer:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_DeviceList:
    def __init__(self, *args, **kwargs) -> None: ...

class TF_Function:
    def __init__(self, *args, **kwargs) -> None: ...

def TFE_AbortCollectiveOps(arg0, arg1: int, arg2: str) -> None: ...
def TFE_CancellationManagerIsCancelled(arg0: TFE_CancellationManager) -> bool: ...
def TFE_CancellationManagerStartCancel(arg0: TFE_CancellationManager) -> None: ...
def TFE_ClearScalarCache() -> object: ...
def TFE_CollectiveOpsCheckPeerHealth(arg0, arg1: str, arg2: int) -> None: ...
def TFE_ContextAddFunction(arg0, arg1: TF_Function) -> None: ...
def TFE_ContextAddFunctionDef(arg0, arg1: str, arg2: int) -> None: ...
def TFE_ContextCheckAlive(arg0, arg1: str) -> bool: ...
def TFE_ContextClearCaches(arg0) -> None: ...
def TFE_ContextClearExecutors(arg0) -> None: ...
def TFE_ContextDisableGraphCollection(arg0) -> None: ...
def TFE_ContextDisableRunMetadata(arg0) -> None: ...
def TFE_ContextEnableGraphCollection(arg0) -> None: ...
def TFE_ContextEnableRunMetadata(arg0) -> None: ...
def TFE_ContextExportRunMetadata(arg0, arg1: TF_Buffer) -> None: ...
def TFE_ContextGetDevicePlacementPolicy(arg0) -> TFE_ContextDevicePlacementPolicy: ...
def TFE_ContextGetExecutorForThread(arg0) -> TFE_Executor: ...
def TFE_ContextGetFunction(arg0, arg1: str) -> TF_Function: ...
def TFE_ContextGetFunctionDef(arg0, arg1: str, arg2: TF_Buffer) -> None: ...
def TFE_ContextGetGraphDebugInfo(arg0, arg1: str, arg2: TF_Buffer) -> None: ...
def TFE_ContextHasFunction(arg0, arg1: str) -> int: ...
def TFE_ContextListDevices(arg0) -> TF_DeviceList: ...
def TFE_ContextListFunctionNames(arg0) -> List[str]: ...
def TFE_ContextOptionsSetAsync(arg0: TFE_ContextOptions, arg1: int) -> None: ...
def TFE_ContextOptionsSetConfig(arg0: TFE_ContextOptions, arg1: bytes) -> None: ...
def TFE_ContextOptionsSetDevicePlacementPolicy(arg0: TFE_ContextOptions, arg1: TFE_ContextDevicePlacementPolicy) -> None: ...
def TFE_ContextOptionsSetJitCompileRewrite(arg0: TFE_ContextOptions, arg1: bool) -> None: ...
def TFE_ContextOptionsSetRunEagerOpAsFunction(arg0: TFE_ContextOptions, arg1: bool) -> None: ...
def TFE_ContextOptionsSetTfrt(arg0: TFE_ContextOptions, arg1: bool) -> None: ...
def TFE_ContextRemoveFunction(arg0, arg1: str) -> None: ...
def TFE_ContextSetExecutorForThread(arg0, arg1: TFE_Executor) -> None: ...
def TFE_ContextSetJitCompileRewrite(arg0, arg1: bool) -> None: ...
def TFE_ContextSetLogDevicePlacement(arg0, arg1: bool) -> None: ...
def TFE_ContextSetRunEagerOpAsFunction(arg0, arg1: bool) -> None: ...
def TFE_ContextSetServerDef(arg0, arg1: int, arg2: bytes) -> None: ...
def TFE_ContextSetServerDefWithTimeoutAndRetries(arg0, arg1: int, arg2: bytes, arg3: int, arg4: int) -> None: ...
def TFE_ContextSetSoftDevicePlacement(arg0, arg1: bool) -> None: ...
def TFE_ContextSetThreadLocalDevicePlacementPolicy(arg0, arg1: TFE_ContextDevicePlacementPolicy) -> None: ...
def TFE_ContextSyncExecutors(arg0) -> None: ...
def TFE_ContextUpdateServerDef(arg0, arg1: int, arg2: bytes) -> None: ...
def TFE_DeleteConfigKeyValue(arg0, arg1: str) -> None: ...
def TFE_DeleteContext(arg0) -> None: ...
def TFE_DeleteContextOptions(arg0: TFE_ContextOptions) -> None: ...
def TFE_DeleteExecutor(arg0: TFE_Executor) -> None: ...
def TFE_EnableCollectiveOps(arg0, arg1: bytes) -> None: ...
def TFE_ExecutorClearError(arg0: TFE_Executor) -> None: ...
def TFE_ExecutorIsAsync(arg0: TFE_Executor) -> bool: ...
def TFE_ExecutorWaitForAllPendingNodes(arg0: TFE_Executor) -> None: ...
def TFE_FromDlpackCapsule(arg0, arg1) -> object: ...
def TFE_GetConfigKeyValue(arg0, arg1: str, arg2: int, arg3: TF_Buffer) -> None: ...
def TFE_GetContextId(arg0) -> int: ...
def TFE_GetMemoryInfo(arg0, arg1: str) -> Dict[str,int]: ...
def TFE_GetTaskStates(arg0, arg1: List[str], arg2: List[int]) -> object: ...
def TFE_HostAddressSpace(arg0, arg1: TF_Buffer) -> None: ...
def TFE_InsertConfigKeyValue(arg0, arg1: str, arg2: str) -> None: ...
def TFE_MonitoringBoolGaugeCellSet(arg0: TFE_MonitoringBoolGaugeCell, arg1: bool) -> None: ...
def TFE_MonitoringBoolGaugeCellValue(arg0: TFE_MonitoringBoolGaugeCell) -> bool: ...
def TFE_MonitoringCounterCellIncrementBy(arg0: TFE_MonitoringCounterCell, arg1: int) -> None: ...
def TFE_MonitoringCounterCellValue(arg0: TFE_MonitoringCounterCell) -> int: ...
def TFE_MonitoringDeleteBoolGauge0(arg0: TFE_MonitoringBoolGauge0) -> None: ...
def TFE_MonitoringDeleteBoolGauge1(arg0: TFE_MonitoringBoolGauge1) -> None: ...
def TFE_MonitoringDeleteBoolGauge2(arg0: TFE_MonitoringBoolGauge2) -> None: ...
def TFE_MonitoringDeleteBuckets(arg0: TFE_MonitoringBuckets) -> None: ...
def TFE_MonitoringDeleteCounter0(arg0: TFE_MonitoringCounter0) -> None: ...
def TFE_MonitoringDeleteCounter1(arg0: TFE_MonitoringCounter1) -> None: ...
def TFE_MonitoringDeleteCounter2(arg0: TFE_MonitoringCounter2) -> None: ...
def TFE_MonitoringDeleteIntGauge0(arg0: TFE_MonitoringIntGauge0) -> None: ...
def TFE_MonitoringDeleteIntGauge1(arg0: TFE_MonitoringIntGauge1) -> None: ...
def TFE_MonitoringDeleteIntGauge2(arg0: TFE_MonitoringIntGauge2) -> None: ...
def TFE_MonitoringDeleteSampler0(arg0: TFE_MonitoringSampler0) -> None: ...
def TFE_MonitoringDeleteSampler1(arg0: TFE_MonitoringSampler1) -> None: ...
def TFE_MonitoringDeleteSampler2(arg0: TFE_MonitoringSampler2) -> None: ...
def TFE_MonitoringDeleteStringGauge0(arg0: TFE_MonitoringStringGauge0) -> None: ...
def TFE_MonitoringDeleteStringGauge1(arg0: TFE_MonitoringStringGauge1) -> None: ...
def TFE_MonitoringDeleteStringGauge2(arg0: TFE_MonitoringStringGauge2) -> None: ...
def TFE_MonitoringDeleteStringGauge3(arg0: TFE_MonitoringStringGauge3) -> None: ...
def TFE_MonitoringDeleteStringGauge4(arg0: TFE_MonitoringStringGauge4) -> None: ...
def TFE_MonitoringGetCellBoolGauge0(arg0: TFE_MonitoringBoolGauge0) -> TFE_MonitoringBoolGaugeCell: ...
def TFE_MonitoringGetCellBoolGauge1(arg0: TFE_MonitoringBoolGauge1, arg1: str) -> TFE_MonitoringBoolGaugeCell: ...
def TFE_MonitoringGetCellBoolGauge2(arg0: TFE_MonitoringBoolGauge2, arg1: str, arg2: str) -> TFE_MonitoringBoolGaugeCell: ...
def TFE_MonitoringGetCellCounter0(arg0: TFE_MonitoringCounter0) -> TFE_MonitoringCounterCell: ...
def TFE_MonitoringGetCellCounter1(arg0: TFE_MonitoringCounter1, arg1: str) -> TFE_MonitoringCounterCell: ...
def TFE_MonitoringGetCellCounter2(arg0: TFE_MonitoringCounter2, arg1: str, arg2: str) -> TFE_MonitoringCounterCell: ...
def TFE_MonitoringGetCellIntGauge0(arg0: TFE_MonitoringIntGauge0) -> TFE_MonitoringIntGaugeCell: ...
def TFE_MonitoringGetCellIntGauge1(arg0: TFE_MonitoringIntGauge1, arg1: str) -> TFE_MonitoringIntGaugeCell: ...
def TFE_MonitoringGetCellIntGauge2(arg0: TFE_MonitoringIntGauge2, arg1: str, arg2: str) -> TFE_MonitoringIntGaugeCell: ...
def TFE_MonitoringGetCellSampler0(arg0: TFE_MonitoringSampler0) -> TFE_MonitoringSamplerCell: ...
def TFE_MonitoringGetCellSampler1(arg0: TFE_MonitoringSampler1, arg1: str) -> TFE_MonitoringSamplerCell: ...
def TFE_MonitoringGetCellSampler2(arg0: TFE_MonitoringSampler2, arg1: str, arg2: str) -> TFE_MonitoringSamplerCell: ...
def TFE_MonitoringGetCellStringGauge0(arg0: TFE_MonitoringStringGauge0) -> TFE_MonitoringStringGaugeCell: ...
def TFE_MonitoringGetCellStringGauge1(arg0: TFE_MonitoringStringGauge1, arg1: str) -> TFE_MonitoringStringGaugeCell: ...
def TFE_MonitoringGetCellStringGauge2(arg0: TFE_MonitoringStringGauge2, arg1: str, arg2: str) -> TFE_MonitoringStringGaugeCell: ...
def TFE_MonitoringGetCellStringGauge3(arg0: TFE_MonitoringStringGauge3, arg1: str, arg2: str, arg3: str) -> TFE_MonitoringStringGaugeCell: ...
def TFE_MonitoringGetCellStringGauge4(arg0: TFE_MonitoringStringGauge4, arg1: str, arg2: str, arg3: str, arg4: str) -> TFE_MonitoringStringGaugeCell: ...
def TFE_MonitoringIntGaugeCellSet(arg0: TFE_MonitoringIntGaugeCell, arg1: int) -> None: ...
def TFE_MonitoringIntGaugeCellValue(arg0: TFE_MonitoringIntGaugeCell) -> int: ...
def TFE_MonitoringNewBoolGauge0(arg0: str, arg1: str) -> TFE_MonitoringBoolGauge0: ...
def TFE_MonitoringNewBoolGauge1(arg0: str, arg1: str, arg2: str) -> TFE_MonitoringBoolGauge1: ...
def TFE_MonitoringNewBoolGauge2(arg0: str, arg1: str, arg2: str, arg3: str) -> TFE_MonitoringBoolGauge2: ...
def TFE_MonitoringNewCounter0(arg0: str, arg1: str) -> TFE_MonitoringCounter0: ...
def TFE_MonitoringNewCounter1(arg0: str, arg1: str, arg2: str) -> TFE_MonitoringCounter1: ...
def TFE_MonitoringNewCounter2(arg0: str, arg1: str, arg2: str, arg3: str) -> TFE_MonitoringCounter2: ...
def TFE_MonitoringNewExponentialBuckets(arg0: float, arg1: float, arg2: int) -> TFE_MonitoringBuckets: ...
def TFE_MonitoringNewIntGauge0(arg0: str, arg1: str) -> TFE_MonitoringIntGauge0: ...
def TFE_MonitoringNewIntGauge1(arg0: str, arg1: str, arg2: str) -> TFE_MonitoringIntGauge1: ...
def TFE_MonitoringNewIntGauge2(arg0: str, arg1: str, arg2: str, arg3: str) -> TFE_MonitoringIntGauge2: ...
def TFE_MonitoringNewSampler0(arg0: str, arg1: TFE_MonitoringBuckets, arg2: str) -> TFE_MonitoringSampler0: ...
def TFE_MonitoringNewSampler1(arg0: str, arg1: TFE_MonitoringBuckets, arg2: str, arg3: str) -> TFE_MonitoringSampler1: ...
def TFE_MonitoringNewSampler2(arg0: str, arg1: TFE_MonitoringBuckets, arg2: str, arg3: str, arg4: str) -> TFE_MonitoringSampler2: ...
def TFE_MonitoringNewStringGauge0(arg0: str, arg1: str) -> TFE_MonitoringStringGauge0: ...
def TFE_MonitoringNewStringGauge1(arg0: str, arg1: str, arg2: str) -> TFE_MonitoringStringGauge1: ...
def TFE_MonitoringNewStringGauge2(arg0: str, arg1: str, arg2: str, arg3: str) -> TFE_MonitoringStringGauge2: ...
def TFE_MonitoringNewStringGauge3(arg0: str, arg1: str, arg2: str, arg3: str, arg4: str) -> TFE_MonitoringStringGauge3: ...
def TFE_MonitoringNewStringGauge4(arg0: str, arg1: str, arg2: str, arg3: str, arg4: str, arg5: str) -> TFE_MonitoringStringGauge4: ...
def TFE_MonitoringSamplerCellAdd(arg0: TFE_MonitoringSamplerCell, arg1: float) -> None: ...
def TFE_MonitoringSamplerCellValue(arg0: TFE_MonitoringSamplerCell, arg1: TF_Buffer) -> None: ...
def TFE_MonitoringStringGaugeCellSet(arg0: TFE_MonitoringStringGaugeCell, arg1: str) -> None: ...
def TFE_MonitoringStringGaugeCellValue(arg0: TFE_MonitoringStringGaugeCell, arg1: TF_Buffer) -> None: ...
def TFE_NewCancellationManager() -> TFE_CancellationManager: ...
def TFE_NewContext(arg0: TFE_ContextOptions) -> object: ...
def TFE_NewContextOptions() -> TFE_ContextOptions: ...
def TFE_NewExecutor(arg0: bool, arg1: bool, arg2: int) -> TFE_Executor: ...
def TFE_OpNameGetAttrType(arg0, arg1: str, arg2: str) -> object: ...
def TFE_Py_EnableInteractivePythonLogging() -> None: ...
def TFE_Py_Execute(arg0, arg1: str, arg2: str, arg3, arg4, arg5) -> object: ...
def TFE_Py_ExecuteCancelable(arg0, arg1: str, arg2: str, arg3, arg4, arg5: TFE_CancellationManager, arg6) -> object: ...
def TFE_Py_FastPathExecute(*args) -> object: ...
def TFE_Py_ForwardAccumulatorJVP(arg0, arg1) -> object: ...
def TFE_Py_ForwardAccumulatorNew(arg0: bool) -> object: ...
def TFE_Py_ForwardAccumulatorPopState() -> object: ...
def TFE_Py_ForwardAccumulatorPushState() -> object: ...
def TFE_Py_ForwardAccumulatorSetAdd(arg0) -> object: ...
def TFE_Py_ForwardAccumulatorSetRemove(arg0) -> None: ...
def TFE_Py_ForwardAccumulatorWatch(arg0, arg1, arg2) -> None: ...
def TFE_Py_InitEagerTensor(arg0) -> object: ...
def TFE_Py_IsCustomDevice(arg0, arg1: str) -> bool: ...
def TFE_Py_PackEagerTensors(arg0, arg1) -> object: ...
def TFE_Py_PackJVPs(arg0) -> object: ...
def TFE_Py_RecordGradient(arg0, arg1, arg2, arg3, arg4) -> object: ...
def TFE_Py_RegisterCustomDevice(arg0, arg1, arg2: str, arg3) -> None: ...
def TFE_Py_RegisterExceptionClass(arg0) -> object: ...
def TFE_Py_RegisterFallbackExceptionClass(arg0) -> object: ...
def TFE_Py_RegisterGradientFunction(arg0) -> object: ...
def TFE_Py_RegisterJVPFunction(arg0) -> object: ...
def TFE_Py_RegisterVSpace(arg0) -> object: ...
def TFE_Py_SetCEagerContext(arg0) -> None: ...
def TFE_Py_SetEagerContext(arg0) -> object: ...
def TFE_Py_SetEagerTensorProfiler(arg0) -> object: ...
def TFE_Py_TapeGradient(arg0, arg1, arg2, arg3, arg4, arg5) -> object: ...
def TFE_Py_TapeSetAdd(arg0) -> None: ...
def TFE_Py_TapeSetDeleteTrace(arg0: int) -> None: ...
def TFE_Py_TapeSetIsEmpty() -> object: ...
def TFE_Py_TapeSetIsStopped() -> object: ...
def TFE_Py_TapeSetNew(arg0, arg1) -> object: ...
def TFE_Py_TapeSetPossibleGradientTypes(arg0) -> object: ...
def TFE_Py_TapeSetRecordOperation(arg0, arg1, arg2, arg3, arg4) -> object: ...
def TFE_Py_TapeSetRecordOperationBackprop(arg0, arg1, arg2, arg3) -> object: ...
def TFE_Py_TapeSetRecordOperationForwardprop(arg0, arg1, arg2, arg3, arg4) -> object: ...
def TFE_Py_TapeSetRemove(arg0) -> None: ...
def TFE_Py_TapeSetRestartOnThread() -> None: ...
def TFE_Py_TapeSetShouldRecordBackprop(arg0) -> object: ...
def TFE_Py_TapeSetStopOnThread() -> None: ...
def TFE_Py_TapeVariableAccessed(arg0) -> None: ...
def TFE_Py_TapeWatch(arg0, arg1) -> None: ...
def TFE_Py_TapeWatchVariable(arg0, arg1) -> None: ...
def TFE_Py_TapeWatchedVariables(arg0) -> object: ...
def TFE_Py_TensorShapeOnDevice(arg0, arg1: int) -> object: ...
def TFE_Py_TensorShapeSlice(arg0, arg1: int) -> object: ...
def TFE_Py_UID() -> object: ...
def TFE_Py_VariableWatcherNew() -> object: ...
def TFE_Py_VariableWatcherRemove(arg0) -> None: ...
def TFE_Py_VariableWatcherVariableAccessed(arg0) -> None: ...
def TFE_Py_VariableWatcherWatchedVariables(arg0) -> object: ...
def TFE_ReportErrorToCluster(arg0, arg1: int, arg2: str) -> None: ...
def TFE_ResetMemoryStats(arg0, arg1: str) -> None: ...
def TFE_SetLogicalCpuDevices(arg0, arg1: int, arg2: str) -> None: ...
def TFE_ToDlpackCapsule(arg0): ...
def TFE_WaitAtBarrier(arg0, arg1: str, arg2: int) -> None: ...
def TF_DeleteDeviceList(arg0: TF_DeviceList) -> None: ...
def TF_DeviceListCount(arg0: TF_DeviceList) -> int: ...
def TF_DeviceListName(arg0: TF_DeviceList, arg1: int) -> str: ...
def TF_DeviceListType(arg0: TF_DeviceList, arg1: int) -> str: ...
def TF_EnableMlirBridge(arg0: bool) -> None: ...
def TF_EnableXlaDevices() -> None: ...
def TF_GetCompilerIr(arg0, arg1: str, arg2: str, arg3: str, arg4, arg5) -> bytes: ...
def TF_GetDeviceDetails(arg0: int) -> Dict[str,str]: ...
def TF_GetXlaConstantFoldingDisabled() -> int: ...
def TF_IsMlirBridgeEnabled() -> int: ...
def TF_ListPhysicalDevices() -> object: ...
def TF_ListPluggablePhysicalDevices() -> object: ...
def TF_NewBufferFromString(arg0, arg1: int) -> TF_Buffer: ...
def TF_PickUnusedPortOrDie() -> int: ...
def TF_ResetJitCompilerFlags() -> None: ...
def TF_SetTfXlaCpuGlobalJit(arg0: int) -> int: ...
def TF_SetXlaAutoJitMode(arg0: str) -> None: ...
def TF_SetXlaConstantFoldingDisabled(arg0: int) -> None: ...
def TF_SetXlaEnableLazyCompilation(arg0: int) -> int: ...
def TF_SetXlaMinClusterSize(arg0: int) -> None: ...