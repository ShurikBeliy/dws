export interface CallbackOneParam<T1, T2 = void> {
  (param: T1): T2;
}

