import { useQuery } from "@tanstack/react-query";
import axios from "axios";

export const useGetAllAnalysis = () =>
    useQuery(
        {
            queryKey: ['tracker-analysis'],
            queryFn: async () => {
                const { data } = await axios.get('http://127.0.0.1:8000/api/v1/voucher/analysis');
                return data;
            },
            refetchInterval: 1000 * 60 * 1
        }
    );