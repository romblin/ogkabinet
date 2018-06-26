import axios from 'axios';

const api = axios.create({
  baseURL: '/api/reports/metrika',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  }
});


export default {
  getSourcesSummary(sourceId, dateFrom, dateTo) {
    const params = {
      'source_id': sourceId,
      'date_from': dateFrom,
      'date_to': dateTo
    };

    return api.get('/sources-summary', {params: params});
  }
};