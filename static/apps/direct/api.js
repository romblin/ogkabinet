import axios from 'axios';

const api = axios.create({
  baseURL: '/api/reports/direct',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  }
});

export default {
  getCampaignsReport (campaignId, dateFrom, dateTo) {
    const params = {
      date_from: dateFrom,
      date_to: dateTo,
      campaign_id: campaignId
    };
    return api.get('/campaigns-performance', {params: params});
  }
};