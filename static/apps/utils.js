export function formatDate(date) {
  const day = ('0' + date.getDate()).slice(-2);
  const month = ('0' + (date.getMonth() + 1)).slice(-2);
  const year = date.getFullYear();
  return `${day}.${month}.${year}`;
}

export const defaultDateFormat = '%d.%m.%y' || DATE_FORMAT;

export const djangoDateTimeFormatToJs = format => {
  return format.toLowerCase().replace(/%\w/g, function(format) {
    format = format.replace(/%/,"");
    return format + format;
  });
};

export const getDateFormat = (format = defaultDateFormat) => djangoDateTimeFormatToJs(format);

export const dateFromString = string => {
  const pattern = /^(\d{1,2})\.(\d{1,2})\.(\d{4})$/;
  return new Date(string.replace(pattern,'$3-$2-$1'));
};

export function formatDateToISO(date) {
  return date.toISOString().split('T')[0];
}