export interface CallbackOneParam<T1, T2 = void> {
  (param: T1): T2;
}

export async function http<T>(
  request: RequestInfo
): Promise<HttpResponse<T>> {
  const response: HttpResponse<T> = await fetch(
    request
  );

  try {
    response.parsedBody = await response.json();
  } catch (ex) {}

  if (!response.ok) {
    throw new Error(response.statusText);
  }
  return response;
}

export async function get<T>(
  path: string,
  args: RequestInit = { method: "get" }
): Promise<HttpResponse<T>> {
  return await http<T>(new Request(path, args));
};

export async function post<T, T1=any>(
  path: string,
  body: T1,
  args: RequestInit = { method: "post", body: JSON.stringify(body) }
): Promise<HttpResponse<T>>  {
  return await http<T>(new Request(path, args));
};

export async function put<T, T1=any>(
  path: string,
  body: T1,
  args: RequestInit = { method: "put", body: JSON.stringify(body) }
): Promise<HttpResponse<T>> {
  return await http<T>(new Request(path, args));
};

export function getCurrentUrl():string {
  return window.location.pathname;
}
