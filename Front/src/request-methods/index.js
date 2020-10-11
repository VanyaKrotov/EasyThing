import serverData from './../config.json';

const isDevelopment = process.env.NODE_ENV === 'development';

export const getImageUrl = (path) =>
  (isDevelopment ? serverData.server : '') + '.' + path;

const headers = {
  credentials: 'include',
  headers: {
    'Content-Type': 'application/json'
  }
};

const treatmentResponse = async (response) => {
  const text = await response.text();
  const json = text.length ? JSON.parse(text) : null;
  console.log('network-> ', json);
  if (!response.ok) {
    throw json.detail;
  }

  return json;
};

export const getRequest = async ({ url, isGlobal = false }) =>
  treatmentResponse(
    await fetch(`${isGlobal ? '' : serverData.server}${url}`, {
      ...headers,
      method: 'GET'
    })
  );

export const deleteRequest = async ({ url, isGlobal = false }) =>
  treatmentResponse(
    await fetch(`${isGlobal ? '' : serverData.server}${url}`, {
      ...headers,
      method: 'DELETE'
    })
  );

export const postRequest = async ({ url, data, isGlobal = false }) =>
  treatmentResponse(
    await fetch(`${isGlobal ? '' : serverData.server}${url}`, {
      ...headers,
      method: 'POST',
      body: data ? JSON.stringify(data) : undefined
    })
  );

export const putRequest = async ({ url, data, isGlobal = false }) =>
  treatmentResponse(
    await fetch(`${isGlobal ? '' : serverData.server}${url}`, {
      ...headers,
      method: 'PUT',
      body: data ? JSON.stringify(data) : undefined
    })
  );
